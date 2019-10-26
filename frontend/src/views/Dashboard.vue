<template>
	<div>
		<h2>Hello, {{ $store.state.user.name }}!</h2>
		Daily motivation
		test thing
		cards
	</div>
</template>

<script lang="ts">
import Vue from 'vue';

export default Vue.extend({
	data() {
		return {
			courses: [],
		};
	},
});
</script>

<style lang="scss" scoped>

</style>