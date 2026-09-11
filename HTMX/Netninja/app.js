import express from 'express';
import morgan from 'morgan';

const app = express();
app.use(express.urlencoded({extended: false}))
app.use(express.static('public'));
app.use(morgan('dev'))

app.get('/', (req, res) => {
    res.send({
        "message": "IceIce Day 620"
    }).status(200);
})

app.listen(5050, () => {
    console.log("App listening on port 5050")
})