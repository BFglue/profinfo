<template><div class="mb-4">

    <div class="text-center mt-4 mb-4">
        <h5>Отличный выбор! 👍</h5>
        <h2 class="display-3">Профессия<br>&laquo;ПРОГРАММИСТ&raquo;</h2>
    </div>
    <div class="row">
        <div class="col-4">
            <div class="metrics-caption">
                16
            </div>
            <div class="metrics-text">
                место в рейтинге профессий
            </div>
        </div>
        <div class="col-4 text-center">
            <div class="metrics-caption">
                25 161 ₽
            </div>
            <div class="metrics-text">
                средняя заработная плата в регионе
            </div>
        </div>
        <div class="col-4 text-right">
            <div class="metrics-caption">
                <span class="fa fa-caret-up"></span>
            </div>
            <div class="metrics-text">
                спрос на профессию растёт
            </div>
        </div>
    </div>

    <div class="results">
        <div class="filters">
            <div class="row">
                <div class="col-5">
                    <b-input placeholder="Регион" />
                </div>
                <div class="col-5">
                    <b-input placeholder="Уровень образования" />
                </div>
                <div class="col-2">
                    <b-input placeholder="Цена обучения, до" />
                </div>
            </div>
        </div>

        <h1 class="mt-4 mb-2"><span class="fa fa-university"></span> ВУЗы</h1>
        <div class="row">
            <div class="col-6">
                <b-card class="mb-2">
                    <h5>УРФУ им. Б. Н. Ельцина</h5>
                    <p>
                        <span class="fa fa-star"></span>
                        <span class="fa fa-star"></span>
                        <span class="fa fa-star"></span>
                        <span class="fa fa-star"></span>
                        <span class="fa fa-star"></span>
                    </p>
                    <p>
                        <b>Где:</b> Екатеринбург<br>
                        <b>Как:</b> бюджет или платно.<br>
                        <b>Цена:</b> 40000 — 170000 ₽ в год.
                    </p>
                    <div>
                        <a href="#">5 специальностей</a>
                    </div>
                </b-card>
            </div>
            <div class="col-6">
                <b-card class="mb-2">
                    <h5>УрГПУ</h5>
                    <p>
                        <span class="fa fa-star"></span>
                        <span class="fa fa-star"></span>
                        <span class="fa fa-star"></span>
                        <span class="fa fa-star"></span>
                        <span class="fa fa-star"></span>
                    </p>
                    <p>
                        <b>Где:</b> Екатеринбург<br>
                        <b>Как:</b> бюджет или платно.<br>
                        <b>Цена:</b> 56000 ₽ в год.
                    </p>
                    <div>
                        <a href="#">2 специальности</a>
                    </div>
                </b-card>
            </div>
        </div>
        <div class="row">
            <div class="col-6">
                <b-card class="mb-2">
                    <h5>ЕАИУП</h5>
                    <p>
                        <span class="fa fa-star"></span>
                        <span class="fa fa-star"></span>
                        <span class="fa fa-star"></span>
                        <span class="fa fa-star"></span>
                        <span class="fa fa-star"></span>
                    </p>
                    <p>
                        <b>Где:</b> Екатеринбург<br>
                        <b>Как:</b> платно.<br>
                        <b>Цена:</b> 30000-50000 ₽ в год.
                    </p>
                    <div>
                        <a href="#">3 специальности</a>
                    </div>
                </b-card>
            </div>
            <div class="col-6">
                <b-card class="mb-2">
                    <div class="text-center">
                        <a href="#">Все ВУЗы</a>
                    </div>
                </b-card>
            </div>
        </div>

        <h1><span class="fa fa-graduation-cap mt-4 mb-2"></span> Колледжи</h1>
        <div class="row">
            <div class="col-6">
                <b-card class="mb-2">
                    <h5>УГК имени И. И. Ползунова</h5>
                    <p>
                        <span class="fa fa-star"></span>
                        <span class="fa fa-star"></span>
                        <span class="fa fa-star"></span>
                        <span class="fa fa-star"></span>
                        <span class="fa fa-star"></span>
                    </p>
                    <p>
                        <b>Где:</b> Екатеринбург<br>
                        <b>Как:</b> бюджет или платно.<br>
                        <b>Цена:</b> 24000 — 40000 ₽ в год.
                    </p>
                    <div>
                        <a href="#">5 специальностей</a>
                    </div>
                </b-card>
            </div>
        </div>

        <h1><span class="fa fa-trophy mt-4 mb-2"></span> Подготовка к экзаменам</h1>
        <div class="row">
            <div class="col-6">
                <b-card class="mb-2">
                    <h5><a href="#">Образовательный центр А</a></h5>
                    <p>
                        Экспресс-курсы для поступающих в ВУЗы
                    </p>
                    <div class="mt-2">
                        <b>Срок:</b> 7 дней.<br>
                        <b>Цена:</b> 4000 ₽
                    </div>
                </b-card>
            </div>
            <div class="col-6">
                <b-card class="mb-2">
                    <h5><a href="#">Образовательный центр Б</a></h5>
                    <p>
                        Подготовка к ЕГЭ по математике
                    </p>
                    <div class="mt-2">
                        <b>Срок:</b> 30 дней.<br>
                        <b>Цена:</b> 20000 ₽
                    </div>
                </b-card>
            </div>
        </div>

        <h1><span class="far fa-star mt-4 mb-4"></span> Это интересно</h1>
        <b-media>
            <b-img slot="aside" blank blank-color="#ccc" width="64" alt="placeholder"></b-img>
            <h5 class="mt-0"><a href="#">Кто такие программисты?</a></h5>
            <p>
                Подробный обзор профессии программист.
            </p>
        </b-media>
        <b-media>
            <b-img slot="aside" blank blank-color="#ccc" width="64" alt="placeholder"></b-img>
            <h5 class="mt-0"><a href="#">Тесты на профориентацию</a></h5>
            <p>
                Пройди тесты и узнай, какие профессии подходят тебе больше всего.
            </p>
        </b-media>
        <b-media>
            <b-img slot="aside" blank blank-color="#ccc" width="64" alt="placeholder"></b-img>
            <h5 class="mt-0"><a href="#">Вакансии "Программист"</a></h5>
            <p>
                Состояние рынка труда по выбранной профессии.
            </p>
        </b-media>

    </div>

    <p class="mt-4"><a href="/abiturient/">Узнать о другой профессии</a></p>

</div></template>

<script>
import axios from 'axios'
export default {
    props: ['profession_id'],
    data() {
        return {
            profession_data: {}
        }
    },
    mounted() {
        this.fetchProfession()
    },
    methods: {
        fetchProfession() {
            return axios.get('/abiturient/profession/')
                .then(response => this.profession_data = response.data)
        }
    }
}
</script>

<style>
    .metrics-caption {
        font-size: 5em;
        font-weight: bold;
    }
    .metrics-text {

    }   
    .results {
        margin-top: 1.5em;
    } 
    .filters {
        border-top: 1px solid #ddd;
        border-bottom: 1px solid #ddd;
        margin: 1.5em 0;
        padding: 1.5em 0;
    }
</style>
