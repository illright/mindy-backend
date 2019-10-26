<template>
	<div class="wrapper">
		<div class="form-card">
			<h1>Login</h1>
			<TextField label="e-mail" v-model="email" />
			<TextField label="password" v-model="password" />
			<div class="actions">
				<Button filled @click="login">
					log in
				</Button>
			</div>
			<p>Don't have an account yet? <router-link to="/register">Register here</router-link>.</p>
		</div>
	</div>
</template>

<script lang="ts">
import Vue from 'vue';
import Button from '@/components/Button.vue';
import TextField from '@/components/TextField.vue';

export default Vue.extend({
	components: {
		Button,
		TextField,
	},
	data() {
		return {
			email: '',
			password: '',
		};
	},
	methods: {
		login() {
			this.$store.dispatch('login', {
				email: this.email,
				password: this.password,
			}).then(() => this.$router.push('/'));
		},
	},
});
</script>

<style lang="scss" scoped>
	.wrapper {
		display: flex;
		justify-content: center;
	}

	.form-card {
		padding: 1.5em 3em;
		border-radius: 25px;
		border: 1px solid #4DB39A;

		.text-field {
			margin-bottom: .8em;
			width: 26em;
		}

		.actions {
			margin-top: 2em;
			display: flex;
			justify-content: flex-end;
		}

		a {
			color: #4DB39A;
		}

		p {
			margin-left: 1em;
		}
	}

	h1 {
		font-weight: 600;
		font-size: 24px;
	}
</style>
