import express from 'express';
import morgan from 'morgan';
import createHomepageTemplate from './views/index.js';
import createListTemplate from './views/list.js';

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

app.listen(5050, () => {
    console.log("App listening on port 5050")
})