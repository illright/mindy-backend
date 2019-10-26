<template>
	<div class="wrapper">
		<div class="form-card">
			<h1>Register</h1>
			<TextField label="full name" />
			<TextField label="e-mail" />
			<TextField label="password" />
			<div class="actions">
				<Button filled @click="login">
					register as a student
				</Button>
				<Button filled @click="login">
					register as a teacher
				</Button>
			</div>
			<p>Already have an account? <a href="#">Log in here</a>.</p>
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
	methods: {
		login() {
			this.$store.state.user = {name: 'Lev'};
			this.$router.push('/');
		},
	},
});
</script>

<style lang="scss">
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
			justify-content: space-between;
		}

		a {
			color: #4DB39A;
		}
	}

	h1 {
		font-weight: 600;
		font-size: 24px;
	}
</style>
