<template>
	<div class="dashboard">
		<h2>Hello, {{ $store.state.user.name }}!</h2>
		<q>
			<label>Daily motivation</label>
			To learn is more than to read.
		</q>
		<div class="card question">
			<img class="icon" src="/img/help-circle-grad.svg" />
			<span>Curious to find out your learner type? Take our test and get your learning to a new level.</span>
			<Button>
				take the test!
			</Button>
		</div>
		<header>
			<h3>My Courses</h3>
			<Button>
				all courses
			</Button>
		</header>
		<div class="courses">
			<CourseCard
			  title="Arithmetic Fundamentals"
				:lessonsCompleted=1
				:lessonsTotal=10
				courseUrl="#"
			/>
			<CourseCard
			  title="Arithmetic Fundamentals"
				:lessonsCompleted=1
				:lessonsTotal=10
				courseUrl="#"
			/>
			<CourseCard
			  title="Arithmetic Fundamentals"
				:lessonsCompleted=1
				:lessonsTotal=10
				courseUrl="#"
			/>
			<CourseCard
			  title="Arithmetic Fundamentals"
				:lessonsCompleted=1
				:lessonsTotal=10
				courseUrl="#"
			/>
			<CourseCard
			  title="Arithmetic Fundamentals"
				:lessonsCompleted=1
				:lessonsTotal=10
				courseUrl="#"
			/>
		</div>
		<header>
			<h3>My Interests</h3>
		</header>
	</div>
</template>

<script lang="ts">
import Vue from 'vue';
import Button from '@/components/Button.vue';
import CourseCard from '@/components/CourseCard.vue';

export default Vue.extend({
	components: {Button, CourseCard},
	data() {
		return {
			courses: [],
		};
	},
});
</script>

<style lang="scss" scoped>
.dashboard {
	padding-left: 60px;
	padding-right: 60px;
}

h2 {
	font-size: 35px;
	font-weight: 600;
}

q {
	position: relative;
	background: rgba(0, 0, 0, 0.05);
	padding: 1.5em 1.8em;
	display: flex;
	align-items: flex-start;
	flex-direction: column;
	border-radius: 15px;
	font-size: 18px;
	overflow: hidden;
	margin-bottom: 1em;

	label {
		text-transform: uppercase;
		font-weight: 700;
		font-size: 14px;
		background: -webkit-linear-gradient(0deg, #8DB946 0%, #4DB29A 100%);
		-webkit-background-clip: text;
  	-webkit-text-fill-color: transparent;
		margin-bottom: 1px;
	}

	&::before {
		height: 100%;
		left: 0;
		top: 0;
		width: 10px;
		content: "";
		position: absolute;
		background: linear-gradient(180deg, #D3EBAD 0%, #B3E5D9 100%);
	}

	&::after {
		content: "";
	}
}

.card.question {
	border-radius: 25px;
	border: 1px solid #B3E5D9;
	padding: 1.5em;
	display: flex;
	align-items: center;
	margin-bottom: 1em;

	.icon {
		margin-right: 1em;
	}

	span {
		flex: 1;
	}
}

header {
	display: flex;
	justify-content: space-between;
	align-items: center;

	h3 {
		font-weight: 600;
		font-size: 27px;
	}

	.btn {
		margin-right: 1.5em;
	}
}

.courses {
	display: grid;
	grid-template-columns: 1fr 1fr 1fr;
	gap: 1.5em;
	margin-bottom: 1em;
}
</style>
