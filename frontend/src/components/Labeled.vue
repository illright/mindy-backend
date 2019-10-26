<template>
	<div class="labeled">
		<label>{{ label }}</label>
		<slot />
	</div>
</template>

<script lang="ts">
	import Vue from 'vue';

	export default Vue.extend({
		props: {
			label: {
				type: String,
			},
		},
	});
</script>

<style lang="scss" scoped>
.labeled {
	display: flex;
	flex-direction: column;
	align-items: flex-start;

	label {
		text-transform: uppercase;
		font-weight: 700;
		font-size: 14px;
		background: -webkit-linear-gradient(0deg, #8DB946 0%, #4DB29A 100%);
		-webkit-background-clip: text;
  	-webkit-text-fill-color: transparent;
		margin-bottom: 2px;
	}
}
</style>
