<template><div>
    
    <div class="logo-wrapper text-center">
        <img src="/static/img/logo.png" id="logo" alt="" />
    </div>

    <div class="text-center mt-4 mb-4">
        <h1 class="display-2">Кем ты хочешь стать?</h1>
        <p class="mb-4">Выбери профессию и узнай, где лучше учиться<br>и сколько можно заработать.</p>
        <p><b-input size="lg" class="large-prof-input mb-4" v-focus /></p>
        <p><b-btn size="lg" class="large-prof-btn" variant="primary" :to="{ 'name': 'profession', params: { profession_id: 4 } }">Вперёд, в будущее <span class="fa fa-chevron-right"></span></b-btn></p>
    </div>

</div></template>

<script>
export default {

}
</script>

<style>
    .logo-wrapper {
        margin: 50px 0;
    }
    #logo {
        height: 130px;
    }
    .large-prof-input {
        font-size: 2em;
        text-align: center;
    }
    .large-prof-btn {
        font-size: 1.5em;
        border-radius: 30px;
    }
</style>