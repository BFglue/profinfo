<template><div>
    
    <b-media class="mb-4">
        <b-img slot="aside" width="64" alt="placeholder" src="/static/img/exam.svg"></b-img>
        <h5 class="mt-0"><b-link :to="{ name: 'report-form' }">Отчёт по специальностям</b-link></h5>
        <p>
            Информация об актуальности специальностей с возможностью группировки по регионам.
        </p>
    </b-media>
    <b-media class="mb-4">
        <b-img slot="aside" width="64" alt="placeholder" src="/static/img/approved.svg"></b-img>
        <h5 class="mt-0"><b-link :to="{ name: 'ratings' }">Рейтинги профессий</b-link></h5>
        <p>
            Информация о новых и активно развивающихся профессиях.
        </p>
    </b-media>
    <b-media class="mb-4">
        <b-img slot="aside" width="64" alt="placeholder" src="/static/img/checklist.svg"></b-img>
        <h5 class="mt-0"><b-link :to="{ name: 'history' }">Ранее созданные отчёты</b-link></h5>
        <p>
            Список предыдущих отчётов, сформированных в системе.
        </p>
    </b-media>

</div></template>

<script>
export default {

}
</script>