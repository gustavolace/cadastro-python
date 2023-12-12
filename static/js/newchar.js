import { sendChar, getID } from "./_functions.js";

const form = document.getElementById("charForm");

const id = getID()
sendChar(form, "/register/newchar", id, id);
