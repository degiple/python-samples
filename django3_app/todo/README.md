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

- id
- name
- create_date
- owner

## participants

- id
- project_id
- user_id
  
### Todo

- id
- title
- content
- status
- start_date
- end_date
- create_user
- create_date

## workers

- id
- todo_id
- user_id
