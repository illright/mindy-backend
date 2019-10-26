<template>
	<div class="lesson">
		<Button>
			back to the course
		</Button>
		<h1>Integer Division in Binary</h1>

		<Card>
			<div class="left">
				<nav class="tabs">
	        <label class="tab">
	          <input type="radio" name="tabs">
	          <div class="icon">
	            Audio
	          </div>
	        </label>
	        <label class="tab">
	          <input type="radio" name="tabs" checked>
	          <div class="icon">
	            Video
	          </div>
	        </label>
	        <label class="tab">
	          <input type="radio" name="tabs">
	          <div class="icon">
	            Text
	          </div>
	        </label>
	      </nav>
				<span class="lesson-num">1/10</span>
			</div>
			<div class="right">
				<p>
					Division is the opposite for multiplication, used when you want to divide stuff.<br/>
					Binary is a base that you are too young to understand.<br/>
					So let’s learn division in binary!
				</p>
				<code>1001010 / 1001 = 10110</code>
				<p>Simple, huh?</p>
				<div class="actions">
					<Button>explain more, please</Button>
					<Button>shorter, please</Button>
					<div class="spacer"></div>
					<Button filled>next step</Button>
				</div>
			</div>
		</Card>
	</div>
</template>

<script lang="ts">
	import Vue from 'vue';
	import Card from '@/components/Card.vue';
	import Button from '@/components/Button.vue';

	export default Vue.extend({
		components: {Card, Button},
	});
</script>

<style lang="scss" scoped>
	.tabs input {
		clip: rect(0, 0, 0, 0);
		width: 1px;
		height: 1px;
		margin: -1px;
		overflow: hidden;
		position: absolute;
	}

	.lesson {
		padding-left: 60px;
		padding-right: 60px;

		& > .card {
			display: flex;
		}
	}

	h1 {
		font-weight: 600;
	}

	.left {
		display: flex;
		flex-direction: column;
		justify-content: space-between;
		border-right: 1px solid #ddd;
		padding-right: 2em;
		padding-left: 1em;
	}

	.tabs {
		margin-bottom: 1em;

		.tab {
			text-transform: uppercase;
			font-weight: 700;
		}

		.icon {
			padding: .5em;
		}

		input:checked + .icon {
			background: -webkit-linear-gradient(0deg, #8DB946 0%, #4DB29A 100%);
			-webkit-background-clip: text;
			-webkit-text-fill-color: transparent;
		}
	}

	.lesson-num {
		padding: .5em;
	}

	.right {
		padding-left: 2em;
		flex: 1;
	}

	code {
		border-radius: 10px;
		background: rgba(0, 0, 0, .05);
		padding: 1.5em;
		margin: 1em 0;
		display: block;
	}

	.actions {
		display: flex;

		.spacer {
			flex: 1;
		}
	}
</style>
