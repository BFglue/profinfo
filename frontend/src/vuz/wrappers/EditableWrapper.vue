<template>
    <span></span>
</template>


<script>
export default {
    props: {'value': '', 'inputclass': ''},
    data () {
        return {
            inner_value: ''
        }
    },
    mounted () {
        this.inner_value = this.value;
        $(this.$el).text(this.value).editable({
            mode: 'inline',
            showbuttons: false,
            inputclass: this.inputclass
        }).on('save', (e, v) => this.inner_value = v.newValue);
    },
    watch: {
        inner_value () {
            this.$emit('edited', this.inner_value);
        },
        value () {
            this.inner_value = this.value
            console.log("helo edit1")
            $(this.$el).text(this.value).editable({
                value: this.value
            })
        }
    }
}
</script>
