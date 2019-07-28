<template>
    <div>
        <select class="form-control" style="width: 100%">
            <!-- <option v-for="option in options" :value="option.id">{{ option.text }}</option> -->
            <slot></slot>
        </select>
    </div>
</template>


<script>
export default {
    props: ['options', 'value'],
    data () {
        return {
            // sections: [],
            // category_id: 0
        }
    },
    mounted: function() {
        const mySelect = $(this.$el).find('select');
        const vm = this
        mySelect.select2()
            .on('change', function () {
                vm.$emit('selectChanged', this.value);
            })
            .val(this.value)
            .trigger('change');
    },
    watch: {
        value: function (value) {
            $(this.$el).find('select').val(value).trigger('change');
            // console.log(value)
        },
        // options: function (options) {
        //     // update options
        //     $(this.$el).empty().select2({ data: options })
        // }
    }
}
</script>
