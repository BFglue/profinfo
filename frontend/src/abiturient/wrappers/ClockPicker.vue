<template>
    <input type="text" class="form-control xenon-clockpicker">
</template>

<script>
    export default {
        props: {
            value: { default: '' }
        },
        mounted () {
            $(this.$el).clockpicker({
                placement: 'top',
                align: 'left',
                autoclose: true,
                'default': 'now'
            }).on('change', () => {
                this.$emit('input', $(this.$el).prop('value'));
            });
            this.updateTime(this.value);
        },
        watch: {
            value (newTime) {
                this.updateTime(newTime);
            }
        },
        methods: {
            updateTime(newTime) {
                $(this.$el).val(newTime);
            }
        }
    }
</script>