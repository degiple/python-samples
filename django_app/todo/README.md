# Todoアプリの概要

## ユーザーができること

- ユーザーアカウント
  - ユーザーアカウントを登録できる
  - ユーザーアカウントの情報を変更できる
  - ユーザーアカウントを削除できる
- Todo
  - Todoプロジェクトを作成できる
  - Todoプロジェクトに、Todoを作成できる
  - Todoプロジェクトに、他のユーザーを参加させる事ができる
  - 作成したTodoに、Todoプロジェクトに参加しているユーザーを割り当てられる

## データベース設計

### ユーザーアカウント

- Djangoのデフォルトを利用

### project

- project_id
- project_name
- create_date
- participants_id

## participants

- participants_id
- user_id
  
### Todo

- todo_id
- title
- content
- status
- start_date
- end_date
- crate_user_id
- create_date
- workers_id

## workers

- workers_id
- user_id
