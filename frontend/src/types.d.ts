export interface Course {
	id: string;
	name: string;
	teacher: {
		name: string;
		email: string;
	}
}