<template>
    <span>
        <slot></slot>
        <span class="clipboard-data-container">
            <slot name="content"></slot>
        </span>
    </span>
</template>

<script>
    export default {
        props: ['value', 'own'],
        mounted() {
            if (this.value) {
                new Clipboard(this.$el, {
                    text: () => {return this.value}
                })
            }
            else if (this.own) {
                new Clipboard(this.$el, {
                    target: (e) => {
                        return this.$el;
                    }
                })
            }
            else {
                new Clipboard(this.$el, {
                    target: (e) => {
                        return $(this.$el).find('.clipboard-data-container')[0]
                    }
                })
            }
        }
    }
</script>

<style>
    .clipboard-data-container {
        position: absolute;
        width: 1px;
        height: 1px;
        left: -9999px;
    }
</style>