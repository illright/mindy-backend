<template>
	<Button @click="login">Log in</Button>
</template>

<script lang="ts">
import Vue from 'vue';
import Button from '@/components/Button.vue';

export default Vue.extend({
	components: {
		Button,
	},
	methods: {
		login() {
			this.$store.state.user = {name: 'Lev'};
			this.$router.push('/');
		},
	},
});
</script>