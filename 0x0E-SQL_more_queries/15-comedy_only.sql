-- lists all Comedy shows.
SELECT ts.title
FROM tv_shows AS ts INNER JOIN tv_show_genres AS sg
ON ts.id = sg.show_id
INNER JOIN tv_genres AS tg
ON sg.genre_id = tg.id
WHERE tg.name = 'Comedy'
ORDER by ts.title;
