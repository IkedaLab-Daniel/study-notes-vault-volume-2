import { createClient } from "@supabase/supabase-js"
import { cookies } from "next/headers"


const Home = async () => {
  const cookieStore = await cookies()
  const supabase = createClient(cookieStore)

  return (
    <div className="page home">
      <h2>Home</h2>
    </div>
  )
}

export default Home