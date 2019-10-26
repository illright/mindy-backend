<template>
	<div role="group" class="chips">
    <label v-for="chip in chips" class="chip-wrapper">
      <input type="checkbox" :name="groupName">
      <div class="chip">{{ chip.name }}</div>
    </label>
  </div>
</template>

<script lang="ts">
	import Vue from 'vue';

	export default Vue.extend({
		props: {
			chips: {
				type: Array,
				required: true,
			},
			groupName: {
				type: String,
				required: true,
			},
		},
	});
</script>

<style lang="scss" scoped>
	$font-face: 'Open Sans', sans-serif;
	$main-hover-faint: linear-gradient(90deg, #8DB946 0%, #4DB39A 100%);

	.chips {
		display: flex;
		flex-wrap: wrap;
	}

	.chip-wrapper > input {
	  clip: rect(0, 0, 0, 0);
	  width: 1px;
	  height: 1px;
	  margin: -1px;
	  overflow: hidden;
	  position: absolute;
	}

	.chip {
	  border-radius: 1.5625em;
	  background-color: rgba(0, 0, 0, .08);
	  color: #656565;
	  padding: .6em .9em;
	  font-weight: 600;
		position: relative;
		margin-right: .5em;

		&::before {
	    border: 0 solid #fff;
	    content: "";
		}
	}

	input:checked + .chip {
	  background: $main-hover-faint;
	  color: #fff;
		padding-left: 2em;
	}

	input[type="checkbox"]:checked + .chip::before {
    width: 5px;
    height: 9px;
    border-bottom-width: 2px;
    border-right-width: 2px;
    transform: translateY(-50%) rotate(45deg);
    position: absolute;
    left: .9em;
    top: 45%;
	}
</style>
