<template>
  <div class="text-field">
    <label>{{ label }}</label>
    <input type="text" :value="value" @input="$emit('input', $event.target.value)" />
  </div>
</template>

<script lang="ts">
import Vue from 'vue';

export default Vue.extend({
  props: {
    label: {
      type: String,
    },
    value: {
      type: String,
    }
  },
});
</script>

<style lang="scss" scoped>
  .text-field {
    border: 1px solid rgba(38, 40, 64, 0.3);
    box-sizing: border-box;
    border-radius: 15px;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    padding: .5em 1em;

    label {
      font-size: 12px;
      color: #262840;
      text-transform: uppercase;
      font-weight: 600;
      font-family: 'Open Sans';
      margin-bottom: .3em;
    }

    input {
      background: none;
      border: none;
      outline: none;
      font-size: 16px;
      font-family: 'Open Sans';
      width: 100%;
    }

    &:focus-within {
      border-color: #4DB39A;
      label {
        color: #4DB39A;
      }
    }
  }
</style>
