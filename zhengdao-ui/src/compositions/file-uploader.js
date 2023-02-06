export async function uploadFile(file, url) {
	console.log('calluploadfile')
	// set up the request data
	let formData = new FormData()
	console.log('hello'+file.file)
	// formData.append('file', file.file)

	// // track status and upload file
	// file.status = 'loading'
	// let response = await fetch(url, { method: 'POST', body: formData })

	// // change status to indicate the success of the upload request
	// file.status = response.ok

	// return response
	return
}

export function uploadFiles(files, url) {
	return Promise.all(files.map((file) => uploadFile(file, url)))
}

export default function createUploader(url) {
	console.log('call')
	return{
		uploadFile: function (file) {
			return uploadFile(file, url)
		},
		uploadFiles: function (files) {
			return uploadFiles(files, url)
		},
	}

}