<template>
  <div id="app">
    <div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link>
      <Button outline>
        {{ text }}
      </Button>
      <TextField :label="text" v-model="text" />

      <CourseCard
        title="Arithmetic Fundamentals"
        :lessonsCompleted=1
        :lessonsTotal=10
        courseUrl="#"
      />
    </div>
    <router-view/>
  </div>
</template>

<script lang="ts">
  import Vue from 'vue';
  import Button from '@/components/Button.vue';
  import TextField from '@/components/TextField.vue';
  import CourseCard from '@/components/CourseCard.vue';

  export default Vue.extend({
    components: {Button, TextField, CourseCard},
    data() {
      return {
        text: '',
      };
    },
  });
</script>

<style lang="scss">
#app {
  font-family: 'Open Sans', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #262840;
}
#nav {
  padding: 30px;
  a {
    font-weight: bold;
    color: #2c3e50;
    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>
