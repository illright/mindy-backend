<template>
  <button class="btn" :class="{filled, outline}">
    <slot>
      {{ text }}
    </slot>
  </button>
</template>

<script lang="ts">
  import Vue from 'vue';

  export default Vue.extend({
    props: {
      text: {
        type: String,
        required: false,
      },
      filled: {
        type: Boolean,
        default: false,
      },
      outline: {
        type: Boolean,
        default: false,
      },
    },
  });
</script>

<style lang="scss" scoped>
  $font-face: 'Open Sans', sans-serif;

  $main: linear-gradient(90deg, #8DB946 0%, #4DB39A 100%);
  $main-hover: linear-gradient(90deg, lighten(#8DB946, 5%) 0%, lighten(#4DB39A, 5%) 100%);
  $main-hover-faint: linear-gradient(90deg, rgba(211, 235, 173, 0.15) 0%, rgba(179, 230, 217, 0.15) 100%);

  $shadow-1: 0 2px 5px transparentize(black, .86),
             0 1px 5px transparentize(black, .88);

  $shadow-raised: 0 2px 4px -1px transparentize(black, .8),
                  0 3px 5px 0    transparentize(black, .86),
                  0 1px 10px 0   transparentize(black, .88);


  .btn {
    font-family: $font-face;
    font-weight: 600;
    font-size: 1rem;
    color: $main;
    text-decoration: none;
    outline: none;
    background: none;
    padding: .8em 1.1em;
    border-radius: 1.5625em;
    display: flex;
    align-items: center;
    cursor: pointer;

    &.filled {
      background: $main;
      box-shadow: $shadow-1;
      color: #fff;

      &:hover:not(:disabled), &:focus {
        background: $main-hover;
        box-shadow: $shadow-raised;
      }

      & > svg {
        stroke: white;
      }
    }

    &.outline {
      border-image: 1px solid #4DB39A;
      color: #4DB39A;
    }

    &:hover:not(:disabled) {
      &, &.outline {
        background: $main-hover-faint;
        color: #4DB39A;
        -webkit-background-clip: none;
        -webkit-text-fill-color: #4DB39A;
      }
    }

    & > svg {
      stroke: $main;
    }
  }

  button.btn {
    border: none;
  }
</style>
