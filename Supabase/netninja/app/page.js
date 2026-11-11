"use client"

import { useEffect, useState } from "react"
import { createClient } from "@/app/utils/supabase/client"

const Home = () => {
  const [fetchError, setFetchError] = useState(null)
  const [smoothies, setSmoothies] = useState(null)
  const supabase = createClient()

  useEffect(() => {
    const fetchSmoothies = async () => {
      const { data, error } = await supabase
        .from("smoothies")
        .select()

      if (error) {
        setFetchError("Could not fetch the smoothies")
        setSmoothies(null)
        console.log(error)
      }
      if (data) {
        setSmoothies(data)
        setFetchError(null)
        console.log("Smoothies Data Success:")
        console.log(data)
      }
    }

    console.log("Ran: FetchSmoothies()")

    fetchSmoothies()
  }, [])

  return (
    <div className="page home">
      {fetchError && <p>{fetchError}</p>}
      {smoothies && (
        <div className="smoothies">
          {/* order-by buttons */}
          <div className="smoothie-grid">
            {smoothies.map((smoothie) => (
              <p key={smoothie.id}>{smoothie.title}</p>
            ))}
          </div>
        </div>
      )}
    </div>
  )
}

export default Home
