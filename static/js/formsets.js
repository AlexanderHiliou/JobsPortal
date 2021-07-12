let skillForm = document.querySelectorAll(".skill-form")
let skillContainer = document.querySelector("#skill-form-container")
let addButton = document.querySelector("#skill-add")
let totalForms = document.querySelector("#id_form-TOTAL_FORMS")
let formNum = skillForm.length-1

addButton.addEventListener('click', addForm)

console.log(formNum)
function addForm(e){
    e.preventDefault()

    let newForm = skillForm[0].cloneNode(true)
    let formRegex = RegExp(`form-(\\d){1}-`,'g')

    formNum++
    newForm.innerHTML = newForm.innerHTML.replace(formRegex, `form-${formNum}-`)
    container.insertBefore(newForm, addButton)

    totalForms.setAttribute('value', `${formNum+1}`)
}