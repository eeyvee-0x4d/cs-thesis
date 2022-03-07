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
		<form @submit.prevent="onFileSubmit()">
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
						    focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none" id="formFileSm" type="file" ref="fileUpload1" @change="handleFileUpload1($event)">
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
						    focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none" id="formFileSm" type="file" ref="fileUpload2" @change="handleFileUpload2($event)">
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
						    focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none" id="formFileSm" type="file" ref="fileUpload3" @change="handleFileUpload3($event)">
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
						    focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none" id="formFileSm" type="file" ref="fileUpload4" @change="handleFileUpload4($event)">
					  	</div>
					</div>
				</div>
			</div>
			<!-- Upload section end -->

			<!-- Upload button start -->
			<div class="flex justify-end">
				<div class="">
					<button type="button" class="inline-block px-6 pt-2.5 pb-2 bg-blue-600 text-white font-medium text-xs leading-normal uppercase rounded shadow-md hover:bg-blue-700 hover:shadow-lg focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-blue-800 active:shadow-lg transition duration-150 ease-in-out flex align-center" @click="onFileSubmit($event)">
				      	<svg v-if="loading" role="status" class="inline mr-2 w-4 h-4 animate-spin  fill-white-600" viewBox="0 0 100 101" fill="none" xmlns="http://www.w3.org/2000/svg">
						    <path d="M100 50.5908C100 78.2051 77.6142 100.591 50 100.591C22.3858 100.591 0 78.2051 0 50.5908C0 22.9766 22.3858 0.59082 50 0.59082C77.6142 0.59082 100 22.9766 100 50.5908ZM9.08144 50.5908C9.08144 73.1895 27.4013 91.5094 50 91.5094C72.5987 91.5094 90.9186 73.1895 90.9186 50.5908C90.9186 27.9921 72.5987 9.67226 50 9.67226C27.4013 9.67226 9.08144 27.9921 9.08144 50.5908Z" fill="currentColor"/>
						    <path d="M93.9676 39.0409C96.393 38.4038 97.8624 35.9116 97.0079 33.5539C95.2932 28.8227 92.871 24.3692 89.8167 20.348C85.8452 15.1192 80.8826 10.7238 75.2124 7.41289C69.5422 4.10194 63.2754 1.94025 56.7698 1.05124C51.7666 0.367541 46.6976 0.446843 41.7345 1.27873C39.2613 1.69328 37.813 4.19778 38.4501 6.62326C39.0873 9.04874 41.5694 10.4717 44.0505 10.1071C47.8511 9.54855 51.7191 9.52689 55.5402 10.0491C60.8642 10.7766 65.9928 12.5457 70.6331 15.2552C75.2735 17.9648 79.3347 21.5619 82.5849 25.841C84.9175 28.9121 86.7997 32.2913 88.1811 35.8758C89.083 38.2158 91.5421 39.6781 93.9676 39.0409Z" fill="currentFill"/>
						</svg>
						<svg v-else aria-hidden="true" focusable="false" data-prefix="fas" data-icon="download"
				        class="w-3 mr-2" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
					        <path fill="currentColor"
					          d="M216 0h80c13.3 0 24 10.7 24 24v168h87.7c17.8 0 26.7 21.5 14.1 34.1L269.7 378.3c-7.5 7.5-19.8 7.5-27.3 0L90.1 226.1c-12.6-12.6-3.7-34.1 14.1-34.1H192V24c0-13.3 10.7-24 24-24zm296 376v112c0 13.3-10.7 24-24 24H24c-13.3 0-24-10.7-24-24V376c0-13.3 10.7-24 24-24h146.7l49 49c20.1 20.1 52.5 20.1 72.6 0l49-49H488c13.3 0 24 10.7 24 24zm-124 88c0-11-9-20-20-20s-20 9-20 20 9 20 20 20 20-9 20-20zm64 0c0-11-9-20-20-20s-20 9-20 20 9 20 20 20 20-9 20-20z" @click="onFileSubmit($event)">
					        </path>
				      	</svg>
						Upload
					</button>
				</div>
			</div>
			<!-- Upload button end -->
		</form>
		<Toast ref="toastNotif"/>
	</div>
</template>

<script>
	import { defineComponent, ref } from 'vue';
	import axios from 'axios';

	import Toast from '../Core/Toast.vue';

	export default defineComponent({
		name: 'CardUpload',
		components: {
			Toast
		},
		data() {
			return {
				files: {
					'Pfizer': null,
					'Sinovac': null,
					'Astrazeneca': null,
					'Moderna': null
				},
				loading: false
			}
		},
		methods: {
			handleFileUpload1(event) {
				const file = event.target.files[0]
				this.files.Pfizer = file
			},
			handleFileUpload2(event) {
				const file = event.target.files[0]
				this.files.Sinovac = file
			},
			handleFileUpload3(event) {
				const file = event.target.files[0]
				this.files.Astrazeneca = file
			},
			handleFileUpload4(event) {
				const file = event.target.files[0]
				this.files.Moderna = file
			},
			onFileSubmit(event) {
				let formData = new FormData();

				formData.append('Pfizer', this.files.Pfizer);
				formData.append('Sinovac', this.files.Sinovac);
				formData.append('Astrazeneca', this.files.Astrazeneca);
				formData.append('Moderna', this.files.Moderna);

				async function uploadFiles() {

					let response = await axios.post(import.meta.env.VITE_DJANGO_BASE_URL + '/upload/',
						formData,
						{
							headers: {
								'Content-Type': 'multipart/form-data'
							}
						}
					);

					if (response.statusText !== "OK") {
						throw new Error(`HTTP error! status: ${response.status}`)
					};

					return await response;
				}
				this.loading = true
				uploadFiles()
					.then(response => {
						this.loading = false 
						this.$refs.toastNotif.text = "Files are uploaded successfully."
						this.$refs.toastNotif.type = "success"
						this.$refs.toastNotif.show = true
					})
					.catch(e => {
						this.loading= false						
						this.$refs.toastNotif.text = "Something's not right."
						this.$refs.toastNotif.type = "error"
						this.$refs.toastNotif.show = true
					})
			}
		}
	});
</script>