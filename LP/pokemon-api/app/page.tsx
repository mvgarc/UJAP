"use client"

import { useEffect, useState } from "react"
import { getPokemones } from "../services/pokemon"
import PokemonCard from "../components/PokemonCard"

export default function Home() {
  const [pokemones, setPokemones] = useState([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    getPokemones()
      .then(data => {
        setPokemones(data)
        setLoading(false)
      })
      .catch(error => {
        console.error("Error:", error)
        setLoading(false)
      })
  }, [])

  if (loading) {
    return <h1>Cargando Pokémon...</h1>
  }

  return (
    <div style={{ padding: "20px" }}>
      <h1>Lista de Pokémon</h1>

      <div style={{ display: "flex", flexWrap: "wrap", gap: "20px" }}>
        {pokemones.map((pokemon: any, index: number) => (
          <PokemonCard
            key={pokemon.name}
            name={pokemon.name}
            index={index + 1}
          />
        ))}
      </div>
    </div>
  )
}