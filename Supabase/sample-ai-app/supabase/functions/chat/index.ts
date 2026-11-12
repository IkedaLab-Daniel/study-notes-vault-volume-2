// supabase/functions/chat/index.ts
//
// ┌─────────────────────────────────────────────────────────────────────────┐
// │  API KEY ARCHITECTURE — HOW IT WORKS                                    │
// │                                                                         │
// │  Browser  ──►  Next.js API Route  ──►  THIS Edge Function  ──►  OpenAI │
// │                                                                         │
// │  The OPENAI_API_KEY is stored as a Supabase secret:                     │
// │    supabase secrets set OPENAI_API_KEY=sk-...                           │
// │                                                                         │
// │  It is read at runtime via Deno.env.get("OPENAI_API_KEY").              │
// │  It NEVER travels to the browser.                                       │
// │                                                                         │
// │  The caller (Next.js API Route) authenticates using either:             │
// │    - The anon key  (public requests, RLS applies)                       │
// │    - The service-role key  (trusted server-to-server, bypasses RLS)     │
// │                                                                         │
// │  Both are passed as:  Authorization: Bearer <key>                       │
// └─────────────────────────────────────────────────────────────────────────┘

import "jsr:@supabase/functions-js/edge-runtime.d.ts";

const corsHeaders = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Headers": "authorization, x-client-info, apikey, content-type",
};

Deno.serve(async (req: Request) => {
  // Handle CORS preflight
  if (req.method === "OPTIONS") {
    return new Response("ok", { headers: corsHeaders });
  }

  try {
    const { messages } = await req.json();

    // 🔒 The API key lives here — injected by Supabase secrets, never hardcoded
    const openAIKey = Deno.env.get("OPENAI_API_KEY");
    if (!openAIKey) {
      return new Response(
        JSON.stringify({ error: "OpenAI API key not configured" }),
        { status: 500, headers: { ...corsHeaders, "Content-Type": "application/json" } }
      );
    }

    const response = await fetch("https://api.openai.com/v1/chat/completions", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        // ✅ API key added server-side, inside the Edge Function
        "Authorization": `Bearer ${openAIKey}`,
      },
      body: JSON.stringify({
        model: "gpt-4o-mini",
        messages,
        max_tokens: 500,
      }),
    });

    if (!response.ok) {
      const error = await response.text();
      return new Response(
        JSON.stringify({ error: `OpenAI error: ${error}` }),
        { status: response.status, headers: { ...corsHeaders, "Content-Type": "application/json" } }
      );
    }

    const data = await response.json();
    const reply = data.choices[0].message.content;

    return new Response(
      JSON.stringify({ reply }),
      { headers: { ...corsHeaders, "Content-Type": "application/json" } }
    );
  } catch (err) {
    return new Response(
      JSON.stringify({ error: String(err) }),
      { status: 500, headers: { ...corsHeaders, "Content-Type": "application/json" } }
    );
  }
});
