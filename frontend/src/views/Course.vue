<template>
	<div class="course-page">
		<h2>{{ course.name }}</h2>
		<div class="info">
			<Labeled label="provided by">
				<em>{{ course.school }}</em>
			</Labeled>
			<Labeled label="course time">
				<em>{{ course.start_time | date }} – {{ course.end_time | date }}</em>
			</Labeled>
			<Labeled label="teacher">
				<em>{{ course.teacher.name }}</em>
				{{ course.teacher.email }}
			</Labeled>
		</div>
		<div class="courses">
			<Card outline>
				<div class="head">
					<div class="number">7</div>
					<span><b>7</b> lessons completed. Good job!</span>
				</div>
				<Button>
					see the past lessons
				</Button>
			</Card>
			<Card>
				<div class="head">
					<div class="number">8</div>
					<span>Integer division in binary</span>
				</div>
				<Button filled>
					<router-link :to="`/lessons/8`" tag="span">see the lesson</router-link>
				</Button>
				<Labeled label="q&a session">
					18:00, 12 Jan 2019
				</Labeled>
				<Labeled label="practice session">
					18:00, 12 Jan 2019
				</Labeled>
				<Button outline>
					join the practice class
				</Button>
			</Card>
			<Card>
				<div class="head">
					<div class="number">9</div>
					<span>Integer division in ternary</span>
				</div>
				<Button filled>
					see the lesson
				</Button>
				<Labeled label="q&a session">
					18:00, 12 Jan 2019
				</Labeled>
				<Labeled label="practice session">
					18:00, 12 Jan 2019
				</Labeled>
				<Button outline>
					join the practice class
				</Button>
			</Card>
		</div>
		<h2>Performance Tracking</h2>
		<div class="performance">
			<Card>
				<div class="title">Preferred Learning Type</div>
				<img class="icon" src="/img/video-grad.svg" />
				<div class="clarification">You're a visual learner</div>
			</Card>
			<Card>
				<div class="title">Practice Completion Rate</div>
				<div class="large">100%</div>
				<div class="clarification">Outstanding!</div>
			</Card>
			<Card>
				<div class="title">MindCoins</div>
				<div class="large">10</div>
				<div class="clarification">Hard work pays off!</div>
			</Card>
		</div>
	</div>
</template>

<script lang="ts">
	import Vue from 'vue';
	import Labeled from '@/components/Labeled.vue';
	import Card from '@/components/Card.vue';
	import Button from '@/components/Button.vue';
	import { Course } from '@/types';

	export default Vue.extend({
		components: {Labeled, Card, Button},
		data() {
			return {
				course: {teacher: {}} as Course,
			};
		},
		mounted() {
			const id = this.$route.params.id;
			this.$store.dispatch('getCourse', id)
				.then(c => this.course = c);
		},
		filters: {
			date(str: string) {
				if(str == undefined) return '';
				return new Date(str).toDateString();
			}
		}
	});
</script>

<style lang="scss" scoped>
	.course-page {
		padding-left: 60px;
	  padding-right: 60px;
	}

	h2 {
		font-size: 35px;
		font-weight: 600;
	}

	em {
		font-style: normal;
		font-weight: 600;
	}

	.info {
		display: flex;

		.labeled:not(:last-child) {
			margin-right: 5em;
		}
	}

	.courses {
		margin-top: 3em;
	}

	.number {
		width: 48px;
		height: 48px;
		display: flex;
		align-items: center;
		justify-content: center;
		background: linear-gradient(90deg, rgba(211, 235, 173, 0.3) 0%, rgba(179, 230, 217, 0.3) 100%);
		border-radius: 50%;
		font-size: 22px;
	}

	.card {
		display: grid;
		grid-template-columns: auto 1fr auto;
		gap: 1em;
		align-items: center;
		margin-bottom: 1.5em;

		.head {
			display: flex;
			align-items: center;
			grid-column: 1 / 3;

			.number {
				margin-right: 1em;
			}
		}

		& > .btn {
			justify-self: end;
		}
	}

	.performance {
		display: grid;
		gap: 2em;
		grid-template-columns: 1fr 1fr 1fr;

		.card {
			display: flex;
			flex-direction: column;
			align-items: center;

			.title {
				font-weight: 600;
				font-size: 1.3em;
				margin-bottom: 1em;
			}
		}
	}

	.clarification, .large {
		background: -webkit-linear-gradient(0deg, #8DB946 0%, #4DB29A 100%);
		-webkit-background-clip: text;
  	-webkit-text-fill-color: transparent;
		font-weight: 600;
	}

	.large {
		font-size: 3em;
	}

	.large, .icon {
		flex: 1;
		display: flex;
		align-items: center;
	}
</style>
