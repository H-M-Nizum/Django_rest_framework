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


// Create post method or create a new instance for school model.

const createInstance = () => {
    const teacher_name = document.getElementById("teacher").value
    const course_name = document.getElementById("course").value
    const course_duration = document.getElementById("duration").value
    const seat = document.getElementById("seat").value
    console.log(teacher_name)
    console.log(course_name)
    console.log(course_duration)
    console.log(seat)

    // create an object
    const instance = {
        teacher_name,
        course_name,
        course_duration,
        seat,
    }
    console.log('instance : ', instance)
    fetch('http://127.0.0.1:8000/app/create/', {
        method: "POST",
        headers: {"content-type": "application/json"},
        body: JSON.stringify(instance), 
    })
    .then((res) => res.json())
    .then((data) => console.log(data))
    .catch((error) => console.error('Error:', error));
}
