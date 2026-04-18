export default function PokemonCard({ name, index }: any) {
  return (
    <div style={{ border: "1px solid gray", padding: "10px" }}>
      <img
        src={`https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/${index}.png`}
        alt={name}
      />
      <p>{name}</p>
    </div>
  )
}