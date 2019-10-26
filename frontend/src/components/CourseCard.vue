<template>
	<div class="card">
		<div class="header">{{ title }}</div>
		<div class="progress">
			<img class="icon" src="/img/check-square-grad.svg" />
			<span>
				<b>{{ lessonsCompleted }}/{{ lessonsTotal }}</b>
				lessons completed
			</span>
		</div>
		<div class="actions">
			<Button filled>
				continue
			</Button>
		</div>
	</div>
</template>

<script lang="ts">
	import Vue from 'vue';
	import Button from '@/components/Button.vue';

	export default Vue.extend({
		components: {
			Button,
		},
		props: {
			title: {
				type: String,
				required: true,
			},
			lessonsCompleted: {
				type: Number,
				required: true,
			},
			lessonsTotal: {
				type: Number,
				required: true,
			},
			courseUrl: {
				type: String,
				required: true,
			},
		},
	});
</script>

<style lang="scss" scoped>
	$shadow-1: 0 2px 5px transparentize(black, .86),
						 0 1px 5px transparentize(black, .88);

	.card {
		border-radius: 15px;
		box-shadow: $shadow-1;
		display: flex;
		flex-direction: column;
		font-family: 'Open Sans';
		padding: 1.5em;

		.header {
			font-size: 20px;
			font-weight: 600;
			margin-bottom: 1em;
		}

		.progress {
			flex: 1;
			display: flex;
			align-items: center;
			margin-bottom: 1.5em;

			.icon {
				margin-right: .5em;
			}
		}

		.actions {
			display: flex;
			justify-content: flex-end;
		}
	}
</style>
