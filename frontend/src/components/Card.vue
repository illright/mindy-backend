<template>
	<div class="card" :class="{outline}">
		<slot />
	</div>
</template>

<script lang="ts">
	import Vue from 'vue';

	export default Vue.extend({
		props: {
			outline: {
				type: Boolean,
				default: false
			},
		},
	});
</script>

<style lang="scss" scoped>
$shadow-1: 0 2px 5px transparentize(black, .86),
					 0 1px 5px transparentize(black, .88);
.card {
	border-radius: 15px;
	font-family: 'Open Sans';
	padding: 1.5em;
	box-shadow: $shadow-1;

	&.outline {
		box-shadow: none;
		border: 1px solid #4DB39A;
	}
}
</style>
