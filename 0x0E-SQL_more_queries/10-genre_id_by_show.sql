-- Lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
SELECT tv_shows.title, tv_show_genre.genre_id
FROM tv_shows INNER JOIN tv_show_genre
WHERE tv_shows.id = tv_show_genre.show_id
ORDER BY tv_shows.title AND tv_show_genres.genre_id;
