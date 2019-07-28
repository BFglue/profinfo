<template>

    <input
            class="form-control"
            type="text"
            placeholder="Дата">

</template>


<script>

    export default {
        data() {
            return {
                start_date: null,
                end_date: null,
            }
        },
        mounted() {
            const el = $(this.$el);
            const self = this;
            el.daterangepicker({
                buttonClasses: ['btn', 'btn-sm'],
                applyClass: 'btn-danger',
                cancelClass: 'btn-inverse',
                "autoApply": true,
                locale: {
                    cancelLabel: 'Отмена',
                    applyLabel: 'Применить',
                    format: 'DD.MM.YYYY', 
                    "firstDay": 1,
                    "monthNames": [
                        "Январь",
                        "Февраль",
                        "Март",
                        "Апрель",
                        "Май",
                        "Июнь",
                        "Июль",
                        "Август",
                        "Сентябрь",
                        "Октябрь",
                        "Ноябрь",
                        "Декабрь"
                    ],
                    "daysOfWeek": [
                        "Вс",
                        "Пн",
                        "Вт",
                        "Ср",
                        "Чт",
                        "Пт",
                        "Сб"
                    ],
                },
                autoUpdateInput: false
            });
            el.on('apply.daterangepicker', function(ev, picker) {
                let start_date = new Date(el.data('daterangepicker').startDate._d.getTime());
                let end_date = new Date(el.data('daterangepicker').endDate._d.getTime());
                start_date.setUTCHours(23,59,59,999);
                end_date.setUTCHours(23,59,59,999);
//                console.log(start_date.toJSON())
//                console.log(end_date.toJSON())
                self.start_date = start_date.toJSON();
                self.end_date = end_date.toJSON();
                el.val(picker.startDate.format('DD.MM.YYYY') + ' - ' + picker.endDate.format('DD.MM.YYYY'));
                self.emitApply()
            });
            el.on('cancel.daterangepicker', function(ev, picker) {
                $(this).val('');
                self.start_date = null
                self.end_date = null
                self.emitCancel()
            });
        },
        methods: {
            emitApply() {
                this.$emit('change', [this.start_date, this.end_date])
            },
            emitCancel() {
                this.$emit('cancel')
            },
            fillDate(start_date, end_date) {
                const el = $(this.$el);
                el.val(moment(start_date).format('DD.MM.YYYY') + ' - ' + moment(end_date).format('DD.MM.YYYY'));
            }
        },
//        watch: {
//            start_date() {
//                this.emitApply()
//            },
//            end_date() {
//                this.emitApply()
//            }
//        }

    }

</script>