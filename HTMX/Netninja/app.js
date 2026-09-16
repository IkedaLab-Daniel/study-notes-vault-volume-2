import express from 'express';
import morgan from 'morgan';
import createHomepageTemplate from './views/index.js';
import createListTemplate from './views/list.js';
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

    res.send(`<li>${title}, ${author}</li>`).status(201);
})

app.listen(5050, () => {
    console.log("App listening on port 5050")
})