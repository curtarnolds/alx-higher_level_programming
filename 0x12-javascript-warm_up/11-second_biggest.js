#!/usr/bin/node
if (process.argv.length <= 3) {
	console.log(0);
} else {
	const argument = process.argv.map(Number)
		.slice(2, process.argv.length)
		.sort((a, b) => a - b);
	console.log(argument[argument.length - 2]);
}
