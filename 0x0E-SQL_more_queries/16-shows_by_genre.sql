-- Lists all shows, and all genres linked to that show
SELECT ts.title AS title, tg.name AS name
FROM tv_shows AS ts LEFT JOIN tv_show_genres AS sg
ON ts.id = sg.show_id
LEFT JOIN tv_genres AS tg
ON tg.id = sg.genre_id
ORDER BY ts.title, tg.name;
