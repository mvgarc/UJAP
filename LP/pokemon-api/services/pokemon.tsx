export async function getPokemones() {
  const res = await fetch("https://pokeapi.co/api/v2/pokemon")

  const data = await res.json()

  return data.results
}