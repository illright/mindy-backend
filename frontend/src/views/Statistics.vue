<template>
    <div class="statistics-wrapper">
        <h2>{{ courseName }} Overall Statistics</h2>
        <div class="activities">
            <Button
                v-for="act in ['classwork', 'homework', 'home quizzes', 'in-Class Quizzes', 'Class Attendance', 'Online Attendance']"
                filled>
                {{ act }}
            </Button>
        </div>

        <div class="statistics">
            <h3>Overall Performance</h3>
            <h3>Students</h3>
            <div class="graph"></div>
            <div class="graph"></div>
        </div>

        <div class="center">
            <Button filled>practice sessions</Button>
        </div>
    </div>
</template>

<script lang="ts">
    import Vue from 'vue';
    import Button from '@/components/Button.vue';

    export default Vue.extend({
        components: {Button},
        computed: {
            courseName() {
                return 'Some Course';
            },
         },
    });
</script>

<style lang="scss">
    h2, h3 {
        font-weight: 600;
    }

    .activities {
        display: flex;
        flex-wrap: wrap;
        justify-content: space-between;
    }

    .statistics {
        display: grid;
        grid-template-columns: 2fr 1fr;
        column-gap: 2em;
    }

    .graph {
        height: 10em;
        border-radius: 15px;
        border: 1px solid #ddd;
    }

    .center {
        margin-top: 1.5em;
        display: flex;
        justify-content: center;
    }
</style>