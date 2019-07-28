<template>
<div id="app">
    <b-navbar toggleable="md" type="dark" variant="primary">

        <b-navbar-toggle target="nav_collapse"></b-navbar-toggle>

        <b-navbar-brand :to="{ name: 'index' }">Личный кабинет сотрудника ОУ</b-navbar-brand>

        <b-collapse is-nav id="nav_collapse">


            <!-- Right aligned nav items -->
            <b-navbar-nav class="ml-auto">

                <b-nav-item :to="{ name: 'messages' }">
                    <!--<span class="fa fa-envelope"></span> <span class="badge badge-pill badge-light" style="position: relative; top: -1px">3</span>-->
                    <span class="fa fa-envelope"></span> 
                    <!-- <span v-if="new_messages_count == 0" class="badge" style="position: relative; top: -1px">0</span> -->
                    <span v-if="new_messages_count > 0"  class="badge badge-pill badge-light" style="position: relative; top: -1px">{{ new_messages_count }}</span>
                </b-nav-item>

                <!-- <b-nav-item :to="{ name: 'help' }">
                    <span class="fa fa-question-circle"></span> 
                </b-nav-item> -->

                <!--<b-navbar-nav>-->
                    <!--<b-nav-form class="mr-2">-->
                        <!--<b-form-input type="text" placeholder="Поиск"></b-form-input>-->
                    <!--</b-nav-form>-->
                <!--</b-navbar-nav>-->

                <b-nav-item-dropdown right v-if="profile.fio">
                    <template slot="button-content">
                        <span class="fa fa-user"></span>
                        {{ profileShortName }}
                        <!--<span v-if="profile.last_name != ''">{{ profile.last_name }} {{ profile.first_name[0] }}. {{ profile.third_name[0] }}.</span>-->
                        <!--<span v-else>{{ profile.email }}</span>-->
                        <!--(ЛК № {{ profile.uid }})-->
                    </template>
                    <!-- <b-dropdown-item :to="{ name: 'profile' }">Профиль</b-dropdown-item> -->
                    <!-- <b-dropdown-item :to="{ name: 'payments' }">Платежи</b-dropdown-item> -->
                    <b-dropdown-item href="/logout/">Выход</b-dropdown-item>
                </b-nav-item-dropdown>

            </b-navbar-nav>
        </b-collapse>
    </b-navbar>
    <br>
</div>
</template>


<script>

import { mapState, mapGetters } from 'vuex'

export default {
    computed: {
        ...mapState(['profile', 'new_messages_count']),
        ...mapGetters(['profileShortName'])
    }
}
</script>
