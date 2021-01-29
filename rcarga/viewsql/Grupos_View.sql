USE [CrmEuro]
GO


SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE VIEW [dbo].[grupos_view]
as

    SELECT T0.id, T0.username, (T1.firts_name + ' ' + T1.last_name) as 'nombre', T3.name as 'Cargo',
        T5.name

    FROM users T0
        LEFT JOIN user_data T1 on T0.id=T1.user_id
        LEFT JOIN user_cargo T2 on T0.id=T2.user_id
        LEFT JOIN cargo T3 on T3.id=T2.cargo_id
        LEFT JOIN user_group T4 on T0.id= T4.user_id
        LEFT JOIN grupo T5 on T5.id=T4.grupo_id

GO


