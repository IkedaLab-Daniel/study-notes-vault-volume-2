// app/api/chat/route.ts
//
// ┌─────────────────────────────────────────────────────────────────────────┐
// │  WHY THIS FILE EXISTS                                                   │
// │                                                                         │
// │  The browser cannot call the Supabase Edge Function directly with a    │
// │  service-role key — that key would be exposed in browser network tabs. │
// │                                                                         │
// │  Instead:                                                               │
// │    Browser  ──►  POST /api/chat  (this file, runs on Node.js server)   │
// │                      └──►  Supabase Edge Function  ──►  OpenAI         │
// │                                                                         │
// │  Secrets used here (all server-only — no NEXT_PUBLIC_ prefix):         │
// │    SUPABASE_CHAT_FUNCTION_URL   — where the Edge Function lives        │
// │    SUPABASE_SERVICE_ROLE_KEY    — authorises the server→Edge call      │
// │                                                                         │
// │  The browser only ever sees YOUR domain's /api/chat endpoint.          │
// │  The OpenAI key and service-role key are never sent to the browser.    │
// └─────────────────────────────────────────────────────────────────────────┘

export async function POST(req: Request) {
  const { messages } = await req.json();

  const functionUrl = process.env.SUPABASE_CHAT_FUNCTION_URL;
  const serviceRoleKey = process.env.SUPABASE_SERVICE_ROLE_KEY;

  if (!functionUrl || !serviceRoleKey) {
    return Response.json(
      { error: "Server is missing SUPABASE_CHAT_FUNCTION_URL or SUPABASE_SERVICE_ROLE_KEY" },
      { status: 500 }
    );
  }

  const edgeRes = await fetch(functionUrl, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      // ✅ Service-role key added here, on the server — never sent to browser
      "Authorization": `Bearer ${serviceRoleKey}`,
    },
    body: JSON.stringify({ messages }),
  });

  if (!edgeRes.ok) {
    const text = await edgeRes.text();
    return Response.json({ error: text }, { status: edgeRes.status });
  }

  const data = await edgeRes.json();
  return Response.json(data);
}
