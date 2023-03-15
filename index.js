import { PythonShell } from "python-shell";

PythonShell.run('app.py', null).then( results => {
    console.log('Extract Text from PDF');
    console.log(results);
 });

