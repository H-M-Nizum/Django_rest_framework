// Access data in django rest api using javaScript
const accessdata = () => {
    fetch('http://127.0.0.1:8000/app/school/')
    //or  fetch('http://127.0.0.1:8000/app/school/1')
    .then(res => res.json())
    .then(course => {
        console.log(course)
        displaydata(course)
    })
    .catch(err => console.log(err))
}
const displaydata = (course) => {
    let id = 0
    course.forEach(data => {
        id = id + 1
        document.getElementById("tbody").innerHTML += `
        <tr>
            <td>${id}</td>
            <td>${data.teacher_name}</td>
            <td>${data.course_name}</td>
            <td>${data.course_duration}</td>
            <td>${data.seat}</td>
        </tr>
        `
    });

}
accessdata()