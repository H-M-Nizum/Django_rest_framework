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
    let Id = 0
    course.forEach(data => {
        Id = Id + 1
        document.getElementById("tbody").innerHTML += `
        <tr id="${data.id}">
            <td scope="row">${Id}</td>
            <td>${data.teacher_name}</td>
            <td>${data.course_name}</td>
            <td>${data.course_duration}</td>
            <td>${data.seat}</td>
            <td><button type="submit" onclick="deleteModelINstance('${data.id}')">DELETE</button></td>
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
    // console.log(teacher_name)
    // console.log(course_name)
    // console.log(course_duration)
    // console.log(seat)

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


// Access teacher id and this model instance value set in input field
const Access_teacherID = () => {
    const id = document.getElementById("Id").value
    console.log(id)
    fetch(`http://127.0.0.1:8000/app/school/${id}`)
    .then(res => res.json())
    .then(course => {
        console.log(course)

        // set instance value in input field.
        document.getElementById("teacher1").value = course.teacher_name
        document.getElementById("course1").value = course.course_name
        document.getElementById("duration1").value = course.course_duration
        document.getElementById("seat1").value = course.seat
        
    })
    .catch(err => console.log(err))
}

// update model instance data
const Update_model_instance = () => {
    const teacher_name = document.getElementById("teacher1").value
    const course_name = document.getElementById("course1").value
    const course_duration = document.getElementById("duration1").value
    const seat = document.getElementById("seat1").value
    const id = document.getElementById("Id").value

    // create an object
    const instance = {
        id,
        teacher_name,
        course_name,
        course_duration,
        seat,
    }
    console.log('instance : ', instance)
    fetch('http://127.0.0.1:8000/app/create/', {
        method: "PUT",
        headers: {"content-type": "application/json"},
        body: JSON.stringify(instance), 
    })
    .then((res) => res.json())
    .then((data) => console.log(data))
    .catch((error) => console.error('Error:', error));
}


// DELEte model instance 

const deleteModelINstance = (id) => {
    console.log("delete instance", id)
    // i should use modelserializer in my django project for model instance id. 
    // so delete operation is not work .
}