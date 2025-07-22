import React, { useEffect, useState } from 'react';
import axios from 'axios';
import './App.css';
function MovieGallery({ token }) {
const [movies, setMovies] = useState([]);
useEffect(() => {
axios.get('http://localhost:8000/api/movies/', {
headers: {
Authorization: `Bearer ${token}`
}
})
.then(response => {
setMovies(response.data); // guarda las películas en el estado
})
.catch(error => {
console.error('Error al cargar películas:', error);
});
}, [token]);
return (
<div className="gallery">
{movies.map(movie => (
<div className="card" key={movie.id}>
<h3>{movie.title}</h3>
<p><strong>Género:</strong> {movie.genre}</p>
<p><strong>Duración:</strong> {movie.duration} min</p>
<p><strong>Calificación:</strong> {movie.rating}/10</p>
<p>{movie.synopsis}</p>
</div>
))}
</div>
);
}
export default MovieGallery;