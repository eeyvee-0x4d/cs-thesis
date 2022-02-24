<template>
	<div class="border border-4 p-4 rounded-lg">
		<!-- Card title start -->
		<div class="">
			<h1 class="text-base font-bold">
				Upload Dataset
			</h1>
			<hr>
		</div>
		<!-- Card title end -->

		<!-- Upload section start -->
		<div class="flex flex-wrap p-4 place-content-evenly">
			<div class="px-4">
				<div class="flex justify-center">
					<div class="mb-3 w-96">
					    <label for="formFileSm" class="form-label inline-block mb-2 text-gray-700">Pfizer</label>
					    <input class="form-control
					    block
					    w-full
					    px-2
					    py-1
					    text-sm
					    font-normal
					    text-gray-700
					    bg-white bg-clip-padding
					    border border-solid border-gray-300
					    rounded
					    transition
					    ease-in-out
					    m-0
					    focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none" id="formFileSm" type="file">
					</div>
				</div>
			</div>
			<div class="px-4">
				<div class="flex justify-center">
				  	<div class="mb-3 w-96">
					    <label for="formFileSm" class="form-label inline-block mb-2 text-gray-700">Sinovac</label>
					    <input class="form-control
					    block
					    w-full
					    px-2
					    py-1
					    text-sm
					    font-normal
					    text-gray-700
					    bg-white bg-clip-padding
					    border border-solid border-gray-300
					    rounded
					    transition
					    ease-in-out
					    m-0
					    focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none" id="formFileSm" type="file">
				  	</div>
				</div>
			</div>
			<div class="px-4">
				<div class="flex justify-center">
				  	<div class="mb-3 w-96">
					    <label for="formFileSm" class="form-label inline-block mb-2 text-gray-700">AstraZeneca</label>
					    <input class="form-control
					    block
					    w-full
					    px-2
					    py-1
					    text-sm
					    font-normal
					    text-gray-700
					    bg-white bg-clip-padding
					    border border-solid border-gray-300
					    rounded
					    transition
					    ease-in-out
					    m-0
					    focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none" id="formFileSm" type="file">
				  	</div>
				</div>
			</div>
			<div class="px-4">
				<div class="flex justify-center">
				  	<div class="mb-3 w-96">
					    <label for="formFileSm" class="form-label inline-block mb-2 text-gray-700">Moderna</label>
					    <input class="form-control
					    block
					    w-full
					    px-2
					    py-1
					    text-sm
					    font-normal
					    text-gray-700
					    bg-white bg-clip-padding
					    border border-solid border-gray-300
					    rounded
					    transition
					    ease-in-out
					    m-0
					    focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none" id="formFileSm" type="file">
				  	</div>
				</div>
			</div>
		</div>
		<!-- Upload section end -->

		<!-- Upload button start -->
		<div class="flex justify-end">
			<div class="">
				<button type="button" class="inline-block px-6 pt-2.5 pb-2 bg-blue-600 text-white font-medium text-xs leading-normal uppercase rounded shadow-md hover:bg-blue-700 hover:shadow-lg focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-blue-800 active:shadow-lg transition duration-150 ease-in-out flex align-center">
					<svg aria-hidden="true" focusable="false" data-prefix="fas" data-icon="download"
			        class="w-3 mr-2" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
				        <path fill="currentColor"
				          d="M216 0h80c13.3 0 24 10.7 24 24v168h87.7c17.8 0 26.7 21.5 14.1 34.1L269.7 378.3c-7.5 7.5-19.8 7.5-27.3 0L90.1 226.1c-12.6-12.6-3.7-34.1 14.1-34.1H192V24c0-13.3 10.7-24 24-24zm296 376v112c0 13.3-10.7 24-24 24H24c-13.3 0-24-10.7-24-24V376c0-13.3 10.7-24 24-24h146.7l49 49c20.1 20.1 52.5 20.1 72.6 0l49-49H488c13.3 0 24 10.7 24 24zm-124 88c0-11-9-20-20-20s-20 9-20 20 9 20 20 20 20-9 20-20zm64 0c0-11-9-20-20-20s-20 9-20 20 9 20 20 20 20-9 20-20z">
				        </path>
			      	</svg>
					Upload
				</button>
			</div>
		</div>
		<!-- Upload button end -->
	</div>
</template>

<script>
	import { defineComponent } from 'vue';

	export default defineComponent({
		name: 'CardUpload',
		components: {

		}
	});
</script>