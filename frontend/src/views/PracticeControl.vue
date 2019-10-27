<template>
	<div class="control-panel">
		<h1>Problem 2</h1>
		<span class="difficulty">Difficulty: easy</span>
		<p>Two cars meet in the middle of the bridge, find yourself some friends, loser.</p>
		<div class="panel">
			<Button outline>
				<img src="/img/check-grad.svg" class="icon mr" />
				problem solved
			</Button>
			<div class="pair large">
				<Button outline>
					<img src="/img/chevron-up-grad.svg" class="icon" />
					increase difficulty
				</Button>
				<Button outline>
					<img src="/img/chevron-down-grad.svg" class="icon" />
					decrease difficulty
				</Button>
			</div>
			<TextField label="question for the teacher" />
			<div class="pair">
				<Button>
					see answers
					<div class="dot"></div>
				</Button>
				<Button outline>
					ask
				</Button>
			</div>
			<Button outline>
				<img src="/img/x-circle-grad.svg" class="icon mr" />
				leave practice session
			</Button>
		</div>
	</div>
</template>

<script lang="ts">
	import Vue from 'vue';
	import Button from '@/components/Button.vue';
	import TextField from '@/components/TextField.vue';

	export default Vue.extend({
		components: {Button, TextField},
	});
</script>

<style lang="scss" scoped>
	.panel {
		display: flex;
		flex-direction: column;
		align-items: stretch;
	}

	.btn {
		padding: 1em;
	}

	.btn .icon.mr {
		margin-right: .5em;
	}

	.pair {
		display: flex;
		margin: 1em 0;
		justify-content: space-between;

		.btn:first-child {
			margin-right: 1em;
		}
	}

	.pair.large	.btn {
		flex-direction: column;
	}

	.dot {
	  width: .75em;
	  height: .75em;
	  border-radius: 50%;
	  margin-left: .5em;
	  display: inline-block;
		background: rgba(192, 3, 3, 0.5);
	}
</style>
