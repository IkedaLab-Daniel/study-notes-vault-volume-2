import express from 'express';
import morgan from 'morgan';
import createHomepageTemplate from './views/index.js';
import createListTemplate from './views/list.js';
import createBookTemplate from './views/book.js';

import BOOKS_DATA from './data/data.js';


const app = express();
app.use(express.urlencoded({extended: false}))
app.use(express.static('public'));
app.use(morgan('dev'))

app.get('/', (req, res) => {
    res.send(createHomepageTemplate()).status(200);
})

app.get('/books', (req, res) => {
    res.send(createListTemplate());
})

app.post('/books', (req, res) => {
    const {title, author} = req.body;
    const id = Math.random().toString();

    BOOKS_DATA.push(
        {
            id,
            title,
            author
        }
    );

    res.redirect(`/books/${id}`);
})

app.get("/books/:id", (req, res) => {
    const {id} = req.params;
    const book = BOOKS_DATA.find((book) => book.id === id);

    res.send(createBookTemplate(book));
})

app.listen(5050, () => {
    console.log("App listening on port 5050")
})