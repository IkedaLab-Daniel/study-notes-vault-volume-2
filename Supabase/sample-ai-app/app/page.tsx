"use client";

// app/page.tsx — Simple Chatbot UI
//
// DATA FLOW (inspect this in DevTools → Network):
//
//   1. User types a message and hits Send
//   2. Browser POSTs to /api/chat  ← YOUR server (no secrets visible here)
//   3. Next.js API route attaches the service-role key and calls Supabase Edge Function
//   4. Edge Function attaches the OpenAI key and calls OpenAI
//   5. Reply bubbles back up to the browser
//
// Open DevTools → Network → click the /api/chat request.
//   Request Payload:  { messages: [...] }           ← no keys!
//   Response:         { reply: "..." }               ← just the answer
//
// The OpenAI key lives only in:
//   • Supabase dashboard → Project Settings → Edge Function Secrets
//   • (locally) .env.local as OPENAI_API_KEY  ← never sent to browser

import { useState, useRef, useEffect } from "react";

type Role = "user" | "assistant";

interface Message {
  role: Role;
  content: string;
}

export default function ChatPage() {
  const [messages, setMessages] = useState<Message[]>([
    {
      role: "assistant",
      content:
        "Hi! I'm a simple chatbot. Ask me anything — and open DevTools → Network to inspect how the API key never reaches your browser.",
    },
  ]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);
  const bottomRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages, loading]);

  async function send() {
    const text = input.trim();
    if (!text || loading) return;

    const userMessage: Message = { role: "user", content: text };
    const next = [...messages, userMessage];
    setMessages(next);
    setInput("");
    setLoading(true);

    try {
      // ✅ Calling our own Next.js API route — no API key in this request
      const res = await fetch("/api/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ messages: next }),
      });

      const data = await res.json();

      if (!res.ok || data.error) {
        setMessages((m) => [
          ...m,
          { role: "assistant", content: `Error: ${data.error ?? "Unknown error"}` },
        ]);
      } else {
        setMessages((m) => [...m, { role: "assistant", content: data.reply }]);
      }
    } catch (err) {
      setMessages((m) => [
        ...m,
        { role: "assistant", content: `Network error: ${String(err)}` },
      ]);
    } finally {
      setLoading(false);
    }
  }

  function handleKeyDown(e: React.KeyboardEvent<HTMLTextAreaElement>) {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      send();
    }
  }

  return (
    <div className="flex flex-col h-full max-w-2xl mx-auto px-4 py-8">
      {/* Header */}
      <div className="mb-4">
        <h1 className="text-xl font-semibold text-zinc-900 dark:text-zinc-100">
          AI Chatbot — API Key Architecture Demo
        </h1>
        <p className="text-sm text-zinc-500 dark:text-zinc-400 mt-1">
          Open{" "}
          <code className="bg-zinc-100 dark:bg-zinc-800 px-1 rounded text-xs">
            DevTools → Network
          </code>{" "}
          and inspect the <strong>/api/chat</strong> request — no API key is visible.
        </p>
      </div>

      {/* Architecture callout */}
      <div className="mb-4 rounded-lg border border-zinc-200 dark:border-zinc-700 bg-zinc-50 dark:bg-zinc-900 p-4 text-xs font-mono text-zinc-600 dark:text-zinc-400 leading-6">
        <div className="font-semibold text-zinc-800 dark:text-zinc-200 mb-1 text-sm font-sans">
          Key flow (server-side only):
        </div>
        <span className="text-blue-600 dark:text-blue-400">Browser</span>
        {" ──POST /api/chat──► "}
        <span className="text-emerald-600 dark:text-emerald-400">Next.js Route</span>
        {" ──service-role key──► "}
        <span className="text-purple-600 dark:text-purple-400">Supabase Edge Fn</span>
        {" ──OpenAI key──► "}
        <span className="text-orange-600 dark:text-orange-400">OpenAI</span>
      </div>

      {/* Messages */}
      <div className="flex-1 overflow-y-auto space-y-3 mb-4 min-h-0">
        {messages.map((m, i) => (
          <div
            key={i}
            className={`flex ${m.role === "user" ? "justify-end" : "justify-start"}`}
          >
            <div
              className={`max-w-[80%] rounded-2xl px-4 py-2 text-sm leading-relaxed ${
                m.role === "user"
                  ? "bg-zinc-900 text-white dark:bg-zinc-100 dark:text-zinc-900"
                  : "bg-zinc-100 text-zinc-900 dark:bg-zinc-800 dark:text-zinc-100"
              }`}
            >
              {m.content}
            </div>
          </div>
        ))}

        {loading && (
          <div className="flex justify-start">
            <div className="bg-zinc-100 dark:bg-zinc-800 rounded-2xl px-4 py-2 text-sm text-zinc-500">
              <span className="animate-pulse">Thinking…</span>
            </div>
          </div>
        )}

        <div ref={bottomRef} />
      </div>

      {/* Input */}
      <div className="flex gap-2 items-end">
        <textarea
          className="flex-1 resize-none rounded-xl border border-zinc-200 dark:border-zinc-700 bg-white dark:bg-zinc-900 text-zinc-900 dark:text-zinc-100 px-4 py-2.5 text-sm focus:outline-none focus:ring-2 focus:ring-zinc-400 dark:focus:ring-zinc-500"
          rows={2}
          placeholder="Type a message… (Enter to send, Shift+Enter for newline)"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={handleKeyDown}
          disabled={loading}
        />
        <button
          onClick={send}
          disabled={loading || !input.trim()}
          className="rounded-xl bg-zinc-900 dark:bg-zinc-100 text-white dark:text-zinc-900 px-4 py-2.5 text-sm font-medium transition-opacity disabled:opacity-40 hover:opacity-80"
        >
          Send
        </button>
      </div>
    </div>
  );
}
